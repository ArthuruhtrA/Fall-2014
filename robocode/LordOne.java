package SWEN101_04;
import robocode.*;
import java.awt.Color;
import robocode.util.Utils.*;
import java.awt.geom.*;

// API help : http://robocode.sourceforge.net/docs/robocode/robocode/Robot.html

/**
 * LordZero - a robot by (Ari Sanders and Hamza Masood)
 */
public class LordOne extends AdvancedRobot
{
	/**
	 * run: LordZero's default behavior
	 */
	
	public double ticks;
	public boolean onWall;
	public boolean direction;//true == right, false == left
	public boolean missed;	

	public void run() {
		// Initialization of the robot should be put here

		setColors(Color.black, Color.red, Color.black, Color.red, Color.black);
		ticks = getTime();
		setAdjustGunForRobotTurn(true);
		onWall = false;
		direction = true;
		missed = false;
		//double sentry = getSentryBorderSize();

		// Robot main loop
		while(true) {
			int distance = 50;
			long time = getTime();
			double gunHeading = getGunHeading();
			if (getX() > getBattleFieldWidth() / 2){//Right Half
				if (getY() > getBattleFieldHeight() / 2){//Top Right
					//Point gun to 225
					if (gunHeading > 270){
						turnGunLeft(gunHeading - 270);
					}
					else if (gunHeading < 180){
						turnGunRight(225 - gunHeading);
					}
					else {
						turnGunRight(10);
					}
				}
				else {//Bottom Right
					//Point gun to 315
					if (gunHeading > 0 && gunHeading < 90){
						turnGunLeft(gunHeading - 90);
					}
					else if (gunHeading < 270){
						turnGunRight(355 - gunHeading);
					}
					else {
						turnGunRight(10);
					}
				}
			}
			else {//Left Half
				if (getY() > getBattleFieldHeight() / 2){//Top Left
					//Point gun to 135
					if (gunHeading > 180){
						turnGunLeft(gunHeading - 180);
					}
					else if (gunHeading < 90){//Bottom Left
						turnGunRight(135 - gunHeading);
					}
					else {
						turnGunRight(10);
					}
				}
				else {
					//Point gun to 45
					if (gunHeading > 270){
						turnGunRight(gunHeading - 45);
					}
					else if (gunHeading < 90){
						turnGunRight(10);
					}
					else {
						turnGunRight(45 - gunHeading);
					}
				}
			}
			if (onWall){
				//Follow wall
				ahead(distance);
			}
			else {
				back(distance);
			}
			if (time - ticks == 10 && !onWall){
				ticks = time;
				back(distance);
			}
		}
	}

	/**
	 * onScannedRobot: What to do when you see another robot
	 */
	public void onScannedRobot(ScannedRobotEvent e) {
		ticks = getTime();
		stop();
		System.out.println(e.getName() + " Detected.");
		//The following wavesurfing code is from robowiki.net
		double bulletPower = Math.min(3.0,getEnergy());
		double myX = getX();
		double myY = getY();
		double absoluteBearing = getHeadingRadians() + e.getBearingRadians();
		double enemyX = getX() + e.getDistance() * Math.sin(absoluteBearing);
		double enemyY = getY() + e.getDistance() * Math.cos(absoluteBearing);
		double enemyHeading = e.getHeadingRadians();
		double enemyVelocity = e.getVelocity();
 
		double deltaTime = 0;
		double battleFieldHeight = getBattleFieldHeight(), 
	       battleFieldWidth = getBattleFieldWidth();
		double predictedX = enemyX, predictedY = enemyY;
		while((++deltaTime) * (20.0 - 3.0 * bulletPower) < Point2D.Double.distance(myX, myY, predictedX, predictedY)){		
			predictedX += Math.sin(enemyHeading) * enemyVelocity;	
			predictedY += Math.cos(enemyHeading) * enemyVelocity;
			if(	predictedX < 18.0 
			|| predictedY < 18.0
			|| predictedX > battleFieldWidth - 18.0
			|| predictedY > battleFieldHeight - 18.0){
				predictedX = Math.min(Math.max(18.0, predictedX), battleFieldWidth - 18.0);	
				predictedY = Math.min(Math.max(18.0, predictedY), battleFieldHeight - 18.0);
				break;
			}
		}
		double theta = normalAbsoluteAngle(Math.atan2(predictedX - getX(), predictedY - getY()));
 
		setTurnRadarRightRadians(normalRelativeAngle(absoluteBearing - getRadarHeadingRadians()));
		setTurnGunRightRadians(normalRelativeAngle(theta - getGunHeadingRadians()));
		fire(bulletPower);
		//End borrowed code
		resume();
	}

	/**
	 * onHitByBullet: What to do when you're hit by a bullet
	 */
	public void onHitByBullet(HitByBulletEvent e) {
		//Turn scanner towards direction of fire, then scan()
		double bullet = e.getBearing();
		if (bullet > 0){
			turnGunRight(bullet);
		}
		else if (bullet < 0) {
			turnGunLeft(bullet);
		}
		scan();
	}
	
	/**
	 * onHitWall: What to do when you hit a wall
	 */
	public void onHitWall(HitWallEvent e) {
		double bearing = e.getBearing();
		if (bearing == 0 && onWall){
			if (direction){
				turnLeft(90);
			}
			else {
				turnRight(90);
			}
		}
		else if (bearing > 0){
			turnLeft(180 - bearing);
		}
		else {
			turnRight(-180 + bearing);
		}
		//Follow wall;
		if (!onWall){
			turnRight(90);
		}
		onWall = true;
	}	

	public void onHitRobot(HitRobotEvent e) {
		//Assume it fires at us so we also call onHitByBullet()
		System.out.println("Hit by " + e.getName());
		stop();
		smartFire(0, e.getBearing());
		back(getHeight());
		if (direction){
			direction = false;
		}
		else {
			direction = true;
		}
		turnRight(180);
		scan();
		resume();
	}
	
	public void onBulletMissed(BulletMissedEvent e) {
		//If robot misses, limit power of next shot
		missed = true;
	}
	
	public void smartFire(double distance, double bearing) {
		if (distance == getHeight() * 100){
			distance = 50;
		}
		double absoluteBearing = getHeading() + bearing;
		double bearingFromGun = normalRelativeAngleDegrees(absoluteBearing - getGunHeading());
		double absoluteBearingFromGun = Math.abs(bearingFromGun);
		if (absoluteBearingFromGun <= 5 && getGunHeat() == 0){
			if (getEnergy() < 25){
				debugFire(0.5);
			}
			else if (distance < 10){
				debugFire(Rules.MAX_BULLET_POWER);
			}
			else if (distance < 100){
				debugFire(4);
			}
			else if (distance < 300){
				debugFire (2);
			}
			else {
				debugFire(1);
			}
		}
	}
	
	public void debugFire(double power){
		if (missed){
			power /= 2;
			missed = false;
		}
		System.out.println("Firing at " + power + ", " + getEnergy() + " remaining.");
		fire(power);
	}
}

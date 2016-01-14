package SWEN101_04;
import robocode.*;
import java.awt.Color;
import static robocode.util.Utils.*;

// API help : http://robocode.sourceforge.net/docs/robocode/robocode/Robot.html

/**
 * LordZero - a robot by (Ari Sanders and Hamza Masood)
 */
public class LordZero extends Robot
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
		double sentry = getSentryBorderSize();
		double width = getBattleFieldWidth();
		double height = getBattleFieldHeight();

		// Robot main loop
		while(true) {
			int distance = 50;
			long time = getTime();
			
			turnGunRight(10);
			double x = getX();
			double y = getY();

			if (x > width - sentry || x < sentry){
				ahead(10);
			}
			else if (y > height - sentry || y < sentry){
				back(10);
			}
			else {
				back(distance);
			}
			if (time - ticks == 10){
				ticks = time;
				ahead(distance);
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
		smartFire(e.getDistance(), e.getBearing());
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
		//Follow wall
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

using UnityEngine;
using System.Collections;

public class clider : MonoBehaviour {
	public score s;
	public int clideNum;
	public string tag;
	public bool isSuccess = false, isFail = false;

	// Use this for initialization
	void Start () {
		s = GameObject.Find("score").GetComponent<score>();
		clideNum = 0;
		tag = "";
		isSuccess = false;
		isFail = false;
	}
	
	// Update is called once per frame
	void Update () {
	}
	void OnTriggerEnter2D(Collider2D other) {

		if(other.gameObject.tag.Equals("success")) {
			if(!isSuccess) {
				print("===trigger enter==");
				isSuccess = true;
				s.success();
				print ("success");
			}
		} else if(!isFail) {
			print("===trigger enter==");
			isFail = true;
			s.fail();
			print ("fail");
		}
	}

	void OnTriggerExit2D(Collider2D other) {
		print("===trigger exit==");
		isSuccess = false;
	}

	void OnCollisionEnter2D(Collision2D other) { 

		if(other.gameObject.tag.Equals("success")) {
			if(!isSuccess) {
				print("===collision enter==");
				isSuccess = true;
				s.success();
			}
		} else if(!isFail) {
			print("===collision enter==");
			isFail = true;
			s.fail();
		}
	}
	void OnCollisionExit2D(Collision2D coll) {
		print("===collision exit==");
		isSuccess = false;
	}

	public void reset() {
		isSuccess = false;
		isFail = false;
	}
}

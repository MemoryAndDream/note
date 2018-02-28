using UnityEngine;
using System.Collections;

public class bird : MonoBehaviour {
	public Vector2 force = new Vector2(0, 50);
	public Transform trans;
	public Vector3 initPos;
	Rigidbody2D body;

	// Use this for initialization
	void Start () {
		body = gameObject.GetComponent<Rigidbody2D>();
		initPos = gameObject.transform.position;
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetButtonDown("Fire1")){
			body.AddForce(force);
		}
	}

	public void reset() {
		body.isKinematic = true;
		gameObject.transform.position = initPos;
		gameObject.transform.eulerAngles = Vector3.zero;
		GetComponent<Animator>().enabled = true;
	}
}

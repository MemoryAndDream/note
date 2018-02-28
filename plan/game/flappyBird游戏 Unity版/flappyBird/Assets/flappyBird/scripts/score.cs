using UnityEngine;
using System.Collections;

public class score : MonoBehaviour {
	public GameObject gameOver;
	GameObject[] nums;
	int nn= 0;
	// Use this for initialization
	void Start () {
		nums = new GameObject[10];
		nums[0] = transform.Find("b0").gameObject;
		nums[1] = transform.Find("b1").gameObject;
		nums[2] = transform.Find("b2").gameObject;
		nums[3] = transform.Find("b3").gameObject;
		nums[4] = transform.Find("b4").gameObject;
		nums[5] = transform.Find("b5").gameObject;
		nums[6] = transform.Find("b6").gameObject;
		nums[7] = transform.Find("b7").gameObject;
		nums[8] = transform.Find("b8").gameObject;
		nums[9] = transform.Find("b9").gameObject;
		for(int i=1; i<10; i++) {
			nums[i].SetActive(false);
		}
		nn = 0;
	}

	public void success() {
		nn++;
		for(int i=0; i<10; i++) {
			nums[i].SetActive(i==nn);
		}
	}

	public void reset() {
		nn = 0;
		nums[0].SetActive(true);
		for(int i=1; i<10; i++) {
			nums[i].SetActive(false);
		}
	}

	public void fail() {
		gameOver.SetActive(true);
		gameOver.GetComponent<Animator>().SetTrigger("gameover");
//		Time.timeScale= 0;
	}
}

# $Id$
# Authority: dag

%define real_name pycrypto

Summary: Collection of cryptographic algorithms and protocols for python
Name: python-crypto
Version: 2.0
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.amk.ca/python/code/crypto.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.amk.ca/files/python/crypto/pycrypto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python >= 2.2
Requires: python >= 2.2
Obsoletes: pycrypto <= %{version}
Provides: pycrypto <= %{version}

%description
pycrypto is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:

    * Hash functions: MD2, MD4, RIPEMD.
    * Block encryption algorithms: AES, ARC2, Blowfish, CAST, DES, Triple-DES, IDEA, RC5.
    * Stream encryption algorithms: ARC4, simple XOR.
    * Public-key algorithms: RSA, DSA, ElGamal, qNEW.
    * Protocols: All-or-nothing transforms, chaffing/winnowing.
    * Miscellaneous: RFC1751 module for converting 128-key keys into a set of English words, primality testing.

%prep
%setup -n %{real_name}-%{version}

%build
python2 setup.py build

%install
%{__rm} -rf %{buildroot}
python2 setup.py install \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKS ChangeLog LICENSE MANIFEST README TODO
%{_libdir}/python*/site-packages/Crypto/

%changelog
* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 1.9-0.a6
- Initial package. (using DAR)

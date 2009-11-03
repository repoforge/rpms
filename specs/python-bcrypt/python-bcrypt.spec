# $Id$
# Authority: dag
# Upstream: Domenico Andreoli <cavok$tiscali,it>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name py-bcrypt

Summary: Python bindings for OpenBSD's Blowfish password hashing code
Name: python-bcrypt
Version: 0.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.mindrot.org/projects/py-bcrypt/

Source: http://www.mindrot.org/files/py-bcrypt/py-bcrypt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
Requires: python

%description
python-bcrypt is a Python wrapper of OpenBSD's Blowfish password hashing
code, as described in "A Future-Adaptable Password Scheme" by Niels
Provos and David Mazières.

This system hashes passwords using a version of Bruce Schneier's Blowfish
block cipher with modifications designed to raise the cost of off-line
password cracking and frustrate fast hardware implementation. The
computation cost of the algorithm is parametised, so it can be increased
as computers get faster. The intent is to make a compromise of a password
database less likely to result in an attacker gaining knowledge of the
plaintext passwords (e.g. using John the Ripper). 

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE MANIFEST README TODO
%{python_sitearch}/bcrypt/

%changelog
* Fri Nov 30 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)

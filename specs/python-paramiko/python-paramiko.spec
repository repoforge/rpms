# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name paramiko

Summary: SSH2 protocol for Python
Name: python-paramiko
Version: 1.5.2
Release: 1
License: GPL
Group: Development/Python
URL: http://www.lag.net/~robey/paramiko/

Source: http://www.lag.net/paramiko/download/paramiko-%{version}.zip
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2

Provides: paramiko

%description
Paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines.  the module works
by taking a socket-like object that you pass in, negotiating with the remote
server, authenticating (using a password or a given private key), and opening
flow-controled "channels" to the server, which are returned as socket-like
objects. you are responsible for verifying that the server's host key is the
one you expected to see, and you have control over which kinds of encryption
or hashing you prefer (if you care), but all of the heavy lifting is done by
the paramiko module. 

%prep
%setup -n %{real_name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README docs/ tests/ demo*
%{python_sitelib}/paramiko/
#%ghost %{python_sitelib}/paramiko/*.pyo

%changelog
* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 1.5.2-1
- Initial package. (using DAR)

# $Id$

%define real_name      CMF
%define zope_minver    2.5

%define zope_home      %{_prefix}/lib/zope
%define software_home  %{zope_home}/lib/python

Summary: Content Management Framework for the Zope web application server
Name: zope-cmf
Version: 1.4.2
Release: 0.3.fr
License: ZPL
Group: System Environment/Daemons
URL: http://cmf.zope.org/
Source: http://cmf.zope.org/download/%{real_name}-%{version}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: zope >= %{zope_minver}
BuildRequires: python

%description
The Zope Content Management Framework provides a set of services and content
objects useful for building highly dynamic, content-oriented portal sites. As
packaged, the CMF generates a site much like the Zope.org site. The CMF is
intended to be easily customizable, in terms of both the types of content
used and the policies and services it provides.

%prep
%setup -q -n %{real_name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{software_home}/Products
cp -a CMF* DCWorkflow %{buildroot}%{software_home}/Products/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt HISTORY.txt INSTALL.txt LICENSE.txt README.txt docs
%{software_home}/Products/*

%changelog
* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 1.4.2-0.2.fr
- Initial RPM release.


# $Id$

%define real_name      CMFPlone
%define real_version   2.0-rc6
%define zope_minver    2.6.2
%define cmf_minver     1.4.2

%define zope_home      %{_prefix}/lib/zope
%define software_home  %{zope_home}/lib/python

Summary: Content Management System built over Zope's content management framework
Name: plone
Version: 2.0
Release: 0.1.rc6.fr
License: GPL
Group: System Environment/Daemons
Source: http://dl.sf.net/plone/%{real_name}%{real_version}.tar.gz
URL: http://plone.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Requires: zope >= %{zope_minver}, zope-cmf >= %{cmf_minver}
BuildRequires: python

%description
The Zope Content Management Framework provides a set of services and content
objects useful for building highly dynamic, content-oriented portal sites. As
packaged, the CMF generates a site much like the Zope.org site. The CMF is
intended to be easily customizable, in terms of both the types of content
used and the policies and services it provides.

%prep
%setup -q -n %{real_name}-%{real_version}

%build
# Not much, eh? :-)

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{software_home}/Products
cp -a * %{buildroot}%{software_home}/Products/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{software_home}/Products/*
# There's an annoying /usr/local/bin/python in there
%exclude %{software_home}/Products/GroupUserFolder/doc

%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.2.rc6.fr
- Update to 2.0-rc6.

* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.2.rc5.fr
- Initial RPM release.


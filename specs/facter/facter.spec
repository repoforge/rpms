# $Id$
# Authority: dag

%define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

Summary: Ruby module for collecting simple facts about a host operating system
Name: facter
Version: 1.5.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://puppetlabs.com/projects/facter/

Source: http://puppetlabs.com/downloads/facter/facter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby-devel >= 1.8.1
Requires: ruby >= 1.8.1

%description 
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts.

%prep
%setup

%{__perl} -pi.orig -e 's|^#!.*$|#!/usr/bin/ruby|' bin/facter

%build

%install
%{__rm} -rf %{buildroot}
DESTDIR="%{buildroot}" ruby install.rb

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING INSTALL LICENSE README
%{_bindir}/facter
%exclude %{_bindir}/facter.orig
%{ruby_sitelibdir}/facter/
%{ruby_sitelibdir}/facter.rb

%changelog
* Fri Jan 28 2011 Steve Huff <shuff@vecna.org> - 1.5.8-1
- Update to version 1.5.8.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.6-1
- Initial package. (using DAR)

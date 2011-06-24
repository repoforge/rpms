# $Id$
# Authority: dag

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}

%define has_ruby_abi 0%{?fedora} || 0%{?rhel} >= 5
%define has_ruby_noarch %has_ruby_abi

Summary: Ruby module for collecting simple facts about a host operating system
Name: facter
Version: 1.5.9
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{name}/

Source0: http://puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz
Source1: http://puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz.asc
# http://projects.puppetlabs.com/issues/7682
# Improve Scientific Linux support, courtesy of Orion Poplawski
Patch0: http://projects.puppetlabs.com/attachments/download/1388/facter-1.5.9-sl.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%if %has_ruby_noarch
BuildArch: noarch
%endif

BuildRequires: ruby >= 1.8.1

Requires: ruby >= 1.8.1
Requires: which
%if %has_ruby_abi
Requires: ruby(abi) = 1.8
%endif

%description
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
%setup
%patch0 -p1

%{__perl} -pi.orig -e 's|^#!.*$|#!/usr/bin/ruby|' bin/facter

%build

%install
%{__rm} -rf %{buildroot}

ruby install.rb --destdir=%{buildroot} --quick --no-rdoc

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING INSTALL LICENSE README
%{_bindir}/facter
%exclude %{_bindir}/facter.orig
%{ruby_sitelibdir}/facter.rb
%{ruby_sitelibdir}/facter

%changelog
* Thu Jun 23 2011 Yury V. Zaytsev <yury@shurup.com> - 1.5.9-1
- Misc changes to make it easier to sync with EPEL.
- Update to version 1.5.9.

* Fri Jan 28 2011 Steve Huff <shuff@vecna.org> - 1.5.8-1
- Update to version 1.5.8.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.6-1
- Initial package. (using DAR)

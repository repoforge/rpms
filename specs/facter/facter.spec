# $Id$
# Authority: dag

%define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

Summary: Ruby module for collecting simple facts about a host operating system
Name: facter
Version: 1.3.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://reductivelabs.com/projects/facter/

Source: http://reductivelabs.com/downloads/facter/facter-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby-devel >= 1.8.1
Requires: ruby >= 1.8.1

%description 
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
%setup

%{__perl} -pi.orig -e 's|^#!.*$|#!/usr/bin/ruby|' bin/facter

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/facter %{buildroot}%{_bindir}/facter

%{__install} -d -m0755 %{buildroot}%{ruby_sitelibdir}/facter/
%{__install} -p -m0644 lib/*.rb %{buildroot}%{ruby_sitelibdir}
%{__install} -p -m0644 lib/facter/*.rb %{buildroot}%{ruby_sitelibdir}/facter/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING INSTALL LICENSE README
%{_bindir}/facter
%{ruby_sitelibdir}/facter/
%{ruby_sitelibdir}/facter.rb

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.6-1
- Initial package. (using DAR)

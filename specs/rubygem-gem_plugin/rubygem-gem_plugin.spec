# $Id$
# Authority: shuff
# Upstream: Zed A. Shaw <zedshaw$zedshaw,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/gem_plugin-%{version}

%global rubyabi 1.8

Summary: A plugin system based on rubygems
Name: rubygem-gem_plugin

Version: 0.2.3
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/gem_plugin/

Source: http://rubygems.org/downloads/gem_plugin-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(gem_plugin) = %{version}

%description
A plugin system based on rubygems that uses dependencies only.

%prep
%setup -q -c -T

%build
%{__mkdir_p} .%{gemdir}
gem install -V \
	--local \
	--install-dir $(pwd)/%{gemdir} \
	--force --rdoc \
	%{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{gemdir}
%{__cp} -a .%{gemdir}/* %{buildroot}%{gemdir}/


%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mv} %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
find %{buildroot}/%{_bindir} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
%{__rm}dir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG 
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/Manifest
%doc %{geminstdir}/README
%doc %{geminstdir}/gem_plugin.gemspec
%doc %{geminstdir}/test
%doc %{gemdir}/doc/gem_plugin-%{version}
%{_bindir}/*
%{gemdir}/cache/gem_plugin-%{version}.gem
%{gemdir}/specifications/gem_plugin-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/setup.rb
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/resources

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 0.2.3-1
- Initial package.

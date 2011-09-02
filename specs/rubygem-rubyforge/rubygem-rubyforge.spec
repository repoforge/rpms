# $Id$
# Authority: shuff
# Upstream: Ara T Howard <ara.t.howard$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rubyforge-%{version}

%global rubyabi 1.8

Summary: Utility for interacting with RubyForge
Name: rubygem-rubyforge

Version: 2.0.4
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/rubyforge/

Source: http://rubygems.org/downloads/rubyforge-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(json_pure) >= 1.1.7

Provides: rubygem(rubyforge) = %{version}

%description
A script which automates a limited set of rubyforge operations. 

* Run 'rubyforge help' for complete usage. 
* Setup: For first time users AND upgrades to 0.4.0: 
* rubyforge setup (deletes your username and password, so run sparingly!) 
* edit ~/.rubyforge/user-config.yml 
* rubyforge config 
* For all rubyforge upgrades, run 'rubyforge config' to ensure you have latest.

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
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{gemdir}/doc/rubyforge-%{version}
%{_bindir}/*
%{gemdir}/cache/rubyforge-%{version}.gem
%{gemdir}/specifications/rubyforge-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 2.0.4-1
- Initial package.

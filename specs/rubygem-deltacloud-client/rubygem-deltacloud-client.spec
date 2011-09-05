# $Id$
# Authority: shuff
# Upstream: Michal Fojtik <mfojtik$redhat,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/deltacloud-client-%{version}

%global rubyabi 1.8

Summary: Deltacloud REST Client for API
Name: rubygem-deltacloud-client

Version: 0.1.1
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://www.deltacloud.org/

Source: http://rubygems.org/downloads/deltacloud-client-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(nokogiri) >= 1.4.3
Requires: rubygem(rest-client) >= 1.6.1

Provides: rubygem(deltacloud-client) = %{version}

%description
Deltacloud Client is a command-line tool that communicates with the Deltacloud
API.

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
find %{buildroot}%{geminstdir}/lib -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/lib -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/COPYING
%doc %{gemdir}/doc/deltacloud-client-%{version}
%{_bindir}/*
%{gemdir}/cache/deltacloud-client-%{version}.gem
%{gemdir}/specifications/deltacloud-client-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/init.rb
%{geminstdir}/lib
%{geminstdir}/specs

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 0.1.1-1
- Initial package.

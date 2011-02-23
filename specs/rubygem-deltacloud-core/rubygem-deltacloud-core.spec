# $Id$
# Authority: shuff
# Upstream: Michal Fojtik <mfojtik$redhat,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/deltacloud-core-%{version}

%global rubyabi 1.8

Summary: Deltacloud server component
Name: rubygem-deltacloud-core

Version: 0.1.2
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://www.deltacloud.org/

Source: http://rubygems.org/downloads/deltacloud-core-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(active_support)
Requires: rubygem(amazon-ec2)
Requires: rubygem(json) >= 1.1.9
Requires: rubygem(rack-accept) >= 0.4.3
Requires: rubygem(rack) >= 1.0.0
Requires: rubygem(rack) <= 1.1.0
Requires: rubygem(sinatra) >= 0.9.4
Requires: rubygem(haml) >= 2.2.17
Requires: rubygem(rake) >= 0.8.7
Requires: rubygem(right_aws)
Provides: rubygem(deltacloud-core) = %{version}

%description
Start an instance on an internal cloud, then with the same code start another
on EC2 or Rackspace. Deltacloud protects your apps from cloud API changes and
incompatibilities, so you can concentrate on managing cloud instances the way
you want. 

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
%doc %{gemdir}/doc/deltacloud-core-%{version}
%{_bindir}/*
%{gemdir}/cache/deltacloud-core-%{version}.gem
%{gemdir}/specifications/deltacloud-core-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/public
%{geminstdir}/support
%{geminstdir}/views
%{geminstdir}/*.rb
%{geminstdir}/*.ru

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 0.1.2-1
- Initial package.

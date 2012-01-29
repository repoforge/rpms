# $Id$
# Authority: shuff
# Upstream: Tim Sharpe <tim$sharpe,id,au>
# ExclusiveDist: el5 el6

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?ruby_sitearchdir: %define ruby_sitearchdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/puppet-lint-%{version}

%global rubyabi 1.8

Summary: Check Puppet manifests against the Puppet Labs style guide
Name: rubygem-puppet-lint

Version: 0.1.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/puppet-lint/

Source: http://rubygems.org/downloads/puppet-lint-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: puppet
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(puppet-lint) = %{version}

%description
The goal of this project is to implement as many of the recommended Puppet
style guidelines from the Puppet Labs style guide as practical.

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
find %{buildroot}%{geminstdir}/{lib,spec} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{lib,spec} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%doc %{geminstdir}/puppet-lint.gemspec
%doc %{gemdir}/doc/puppet-lint-%{version}
%{_bindir}/*
%{gemdir}/cache/puppet-lint-%{version}.gem
%{gemdir}/specifications/puppet-lint-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/spec

%changelog
* Tue Oct 11 2011 Steve Huff <shuff@vecna.org> - 0.1.6-1
- Initial package.

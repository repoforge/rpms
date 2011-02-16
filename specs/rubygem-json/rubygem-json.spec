# $Id$
# Authority: shuff
# Upstream: Florian Frank

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/json-%{version}

%global rubyabi 1.8

Summary: JSON implementation in C for Ruby
Name: rubygem-json

Version: 1.5.1
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/json/

Source: http://rubygems.org/downloads/json-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(json) = %{version}

%description
This is a implementation of the JSON specification according to RFC 4627. You
can think of it as a low fat alternative to XML, if you want to store data to
disk or transmit it over a network rather than use a verbose markup language. 

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
%doc %{geminstdir}/CHANGES
%doc %{geminstdir}/COPYING*
%doc %{geminstdir}/GPL
%doc %{geminstdir}/README*
%doc %{geminstdir}/TODO
%doc %{geminstdir}/VERSION
%doc %{gemdir}/doc/json-%{version}
%{_bindir}/*
%{gemdir}/cache/json-%{version}.gem
%{gemdir}/specifications/json-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/install.rb
%{geminstdir}/benchmarks
%{geminstdir}/bin
%{geminstdir}/data
%{geminstdir}/ext
%{geminstdir}/java
%{geminstdir}/json-java.gemspec
%{geminstdir}/lib
%{geminstdir}/tests
%{geminstdir}/tools
%exclude %{geminstdir}/.require_paths

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 1.5.1-1
- Initial package.

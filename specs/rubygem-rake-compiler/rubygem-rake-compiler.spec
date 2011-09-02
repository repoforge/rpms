# $Id$
# Authority: shuff
# Upstream: Luis Lavena <luislavena$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rake-compiler-%{version}

%global rubyabi 1.8

Summary: Use Rake to package C and Java extensions for Ruby
Name: rubygem-rake-compiler

Version: 0.7.6
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/rake-compiler/

Source: http://rubygems.org/downloads/rake-compiler-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(rake)

Provides: rubygem(rake-compiler) = %{version}

%description
Provide a standard and simplified way to build and package Ruby extensions (C,
Java) using Rake as glue.

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
%doc %{geminstdir}/Isolate
%doc %{geminstdir}/LICENSE.txt
%doc %{geminstdir}/README.rdoc
%doc %{gemdir}/doc/rake-compiler-%{version}
%{_bindir}/*
%{gemdir}/cache/rake-compiler-%{version}.gem
%{gemdir}/specifications/rake-compiler-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/cucumber.yml
%{geminstdir}/features
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/tasks

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 0.7.6-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Ryan Tomayko <rtomayko$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/tilt-%{version}

%global rubyabi 1.8

Summary: Generic interface to multiple Ruby template engines
Name: rubygem-tilt

Version: 1.2.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/tilt/

Source: http://rubygems.org/downloads/tilt-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(tilt) = %{version}

%description
Tilt is a thin interface over a bunch of different Ruby template engines in an
attempt to make their usage as generic possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):

* Custom template evaluation scopes / bindings
* Ability to pass locals to template evaluation
* Support for passing a block to template evaluation for "yield"
* Backtraces with correct filenames and line numbers
* Template file caching and reloading
* Fast, method-based template source compilation

The primary goal is to get all of the things listed above right for all
template engines included in the distribution.

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
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/README.md
%doc %{geminstdir}/TEMPLATES.md
%doc %{geminstdir}/tilt.gemspec
%doc %{gemdir}/doc/tilt-%{version}
%{_bindir}/*
%{gemdir}/cache/tilt-%{version}.gem
%{gemdir}/specifications/tilt-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 1.2.2-1
- Initial package.

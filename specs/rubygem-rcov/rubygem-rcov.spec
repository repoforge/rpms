# $Id$
# Authority: shuff
# Upstream: Relevance (http://thinkrelevance.com)

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rcov-%{version}

%global rubyabi 1.8

Summary: Ruby code coverage tool
Name: rubygem-rcov

Version: 0.9.9
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/rcov/

Source: http://rubygems.org/downloads/rcov-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(rcov) = %{version}

%description
rcov is a code coverage tool for Ruby. It is commonly used for viewing overall
test unit coverage of target code. It features fast execution (20-300 times
faster than previous tools), multiple analysis modes, XHTML and several kinds
of text reports, easy automation with Rake via a RcovTask, fairly accurate
coverage information through code linkage inference using simple heuristics,
colorblind-friendliness...

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
%doc %{geminstdir}/BLURB
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/THANKS
%doc %{gemdir}/doc/rcov-%{version}
%doc %{geminstdir}/doc
%doc %{geminstdir}/editor-extensions
%{_bindir}/*
%{gemdir}/cache/rcov-%{version}.gem
%{gemdir}/specifications/rcov-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/setup.rb
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 0.9.9-1
- Initial package.

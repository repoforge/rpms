# $Id$
# Authority: shuff
# Upstream: Aaron Patterson <aaron.patterson$gmail,com>
# ExcludeDist: el5

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/racc-%{version}

%global rubyabi 1.8

Summary: Ruby equivalent of yacc/bison
Name: rubygem-racc

Version: 1.4.6
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/racc/

Source: http://rubygems.org/downloads/racc-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(racc) = %{version}

%description
Racc is a LALR(1) parser generator. It is written in Ruby itself, and generates
Ruby programs.

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
find %{buildroot}/%{_bindir} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/local/bin/"#!/usr/bin/ruby"'
%{__rm}dir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/ChangeLog
%doc %{geminstdir}/DEPENDS
%doc %{geminstdir}/README.*
%doc %{geminstdir}/TODO
%doc %{geminstdir}/doc
%doc %{geminstdir}/sample
%doc %{geminstdir}/web
%doc %{gemdir}/doc/racc-%{version}
%{_bindir}/*
%{gemdir}/cache/racc-%{version}.gem
%{gemdir}/specifications/racc-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/fastcache
%{geminstdir}/lib
%{geminstdir}/misc
%{geminstdir}/setup.rb
%{geminstdir}/tasks
%{geminstdir}/test
%exclude %{geminstdir}/.git*
%exclude %{geminstdir}/.require_paths

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 1.4.6-1
- Initial package.

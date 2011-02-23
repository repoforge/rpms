# $Id$
# Authority: shuff
# Upstream: Nathan Sobo <nathansobo$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/treetop-%{version}

%global rubyabi 1.8

Summary: Ruby-based text parsing and interpretation DSL
Name: rubygem-treetop

Version: 1.4.9
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/treetop/

Source: http://rubygems.org/downloads/treetop-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(polyglot) >= 0.3.1
Provides: rubygem(treetop) = %{version}

%description
Treetop is a Ruby-based DSL for text parsing and interpretation. It facilitates
an extension of the object-oriented paradigm called syntax-oriented
programming.

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
find %{buildroot}%{geminstdir}/{doc,lib} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%doc %{geminstdir}/treetop.gemspec
%doc %{gemdir}/doc/treetop-%{version}
%doc %{geminstdir}/doc
%doc %{geminstdir}/examples
%{_bindir}/*
%{gemdir}/cache/treetop-%{version}.gem
%{gemdir}/specifications/treetop-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/spec

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 1.4.9-1
- Initial package.

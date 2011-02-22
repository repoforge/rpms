# $Id$
# Authority: shuff
# Upstream: Hampton Catlin <hcatlin$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/haml-%{version}

%global rubyabi 1.8

Summary: HTML templating language for Ruby
Name: rubygem-haml

Version: 3.0.25
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/haml/

Source: http://rubygems.org/downloads/haml-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(haml) = %{version}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or XML
that's designed to express the structure of XHTML or XML documents in a
non-repetitive, elegant, easy way, using indentation rather than closing tags
and allowing Ruby to be embedded with ease. It was originally envisioned as a
plugin for Ruby on Rails, but it can function as a stand-alone templating
engine. 

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
%doc %{geminstdir}/CONTRIBUTING
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/README.md
%doc %{geminstdir}/REVISION
%doc %{geminstdir}/VERSION
%doc %{geminstdir}/VERSION_NAME
%doc %{gemdir}/doc/haml-%{version}
%{_bindir}/*
%{gemdir}/cache/haml-%{version}.gem
%{gemdir}/specifications/haml-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/extra
%{geminstdir}/lib
%{geminstdir}/rails
%{geminstdir}/test
%{geminstdir}/vendor
%{geminstdir}/*.rb
%exclude %{geminstdir}/.yardopts

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 3.0.25-1
- Initial package.

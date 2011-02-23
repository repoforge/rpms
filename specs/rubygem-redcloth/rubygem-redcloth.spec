# $Id$
# Authority: shuff
# Upstream: Jason Garber <jg$jasongarber,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/RedCloth-%{version}

%global rubyabi 1.8

Summary: Textile parser for Ruby
Name: rubygem-RedCloth

Version: 4.2.7
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://redcloth.org/

Source: http://rubygems.org/downloads/RedCloth-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(RedCloth) = %{version}

%description
RedCloth is a module for using the Textile markup language in Ruby. Textile is
a simple text format that can be converted to HTML, eliminating the need to use
HTML directly to create documents, blogs, or web pages. Textile gives you
readable text while you’re writing and beautiful text for your readers. If you
need to break out into HTML, Textile allows you to do so easily.

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
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/Gemfile
%doc %{geminstdir}/redcloth.gemspec
%doc %{geminstdir}/README.rdoc
%doc %{gemdir}/doc/RedCloth-%{version}
%doc %{geminstdir}/doc
%{_bindir}/*
%{gemdir}/cache/RedCloth-%{version}.gem
%{gemdir}/specifications/RedCloth-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/tasks
%exclude %{geminstdir}/.gemtest
%exclude %{geminstdir}/.require_paths
%exclude %{geminstdir}/.rspec

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 4.2.7-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Christian Neukirchen <chneukirchen$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/rack-%{version}

%global rubyabi 1.8

Summary: Ruby webserver interface
Name: rubygem-rack

Version: 1.1.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rack.rubyforge.org/

Source: http://rubygems.org/downloads/rack-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(rack) = %{version}

%description
Rack provides minimal, modular and adaptable interface for developing web
applications in Ruby. By wrapping HTTP requests and responses in the simplest
way possible, it unifies and distills the API for web servers, web frameworks,
and software in between (the so-called middleware) into a single method call.

%prep
%setup -q -c -T

%build
%{__mkdir_p} .%{gemdir}
gem install -V \
	--local \
	--install-dir $(pwd)/%{gemdir} \
	--force --rdoc \
	%{SOURCE0}

# change some syntax to stop the whining
%{__perl} -pi -e 's|options\.merge! opt_parser\.parse! args|options.merge!(opt_parser.parse!(args))|' .%{geminstdir}/lib/rack/server.rb

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
%doc %{geminstdir}/KNOWN-ISSUES
%doc %{geminstdir}/RDOX
%doc %{geminstdir}/README
%doc %{geminstdir}/SPEC
%doc %{geminstdir}/contrib
%doc %{geminstdir}/example
%doc %{geminstdir}/rack.gemspec
%doc %{gemdir}/doc/rack-%{version}
%{_bindir}/*
%{gemdir}/cache/rack-%{version}.gem
%{gemdir}/specifications/rack-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Tue Feb 22 2011 Steve Huff <shuff@vecna.org> - 1.1.0-1
- Initial package.

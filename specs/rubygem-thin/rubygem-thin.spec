# $Id$
# Authority: shuff
# Upstream: Marc-Andre Cournoyer <macournoyer$yahoo,ca>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/thin-%{version}

%global rubyabi 1.8

Summary: Secure, stable, fast, extensible Ruby web server
Name: rubygem-thin

Version: 1.2.7
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://code.macournoyer.com/thin/

Source: http://rubygems.org/downloads/thin-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(daemons) >= 1.0.9
Requires: rubygem(eventmachine) >= 0.12.6
Requires: rubygem(rack) >= 1.0.0

Provides: rubygem(thin) = %{version}

%description
Thin is a Ruby web server that glues together 3 of the best Ruby libraries in
web history:

* the Mongrel parser, the root of Mongrel speed and security
* Event Machine, a network I/O library with extremely high scalability,
  performance and stability
* Rack, a minimal interface between webservers and Ruby frameworks

Which makes it, with all humility, the most secure, stable, fast and extensible
Ruby web server bundled in an easy to use gem for your own pleasure. 

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
find %{buildroot}/%{geminstdir}/{benchmark,bin,example,spec} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
find %{buildroot}/%{geminstdir}/{benchmark,bin,example,spec} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/bin/env rackup"#!/usr/bin/rackup"'
find %{buildroot}/%{geminstdir}/{example,spec} -type f | xargs -n 1 sed -i  -e 's"/usr/local/bin/ruby"/usr/bin/ruby"'
find %{buildroot}%{geminstdir}/lib -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/lib -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/README
%doc %{geminstdir}/benchmark
%doc %{geminstdir}/example
%doc %{gemdir}/doc/thin-%{version}
%{_bindir}/*
%{gemdir}/cache/thin-%{version}.gem
%{gemdir}/specifications/thin-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/tasks

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 1.2.7-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Alexis Sellier <alexis$cloudhead,net>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/less-%{version}

%global rubyabi 1.8

Summary: Dynamic stylesheet support for Ruby
Name: rubygem-less

Version: 1.2.21
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://lesscss.org/

Source: http://rubygems.org/downloads/less-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(mutter) >= 0.4.2
Requires: rubygem(treetop) >= 1.4.2
Provides: rubygem(less) = %{version}

%description
LESS extends CSS with dynamic behavior such as variables, mixins, operations
and functions. LESS runs on both the client-side (IE 6+, Webkit, Firefox) and
server-side, with Node.js. 

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
find %{buildroot}%{geminstdir}/lib -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%doc %{geminstdir}/VERSION
%doc %{geminstdir}/less.gemspec
%doc %{gemdir}/doc/less-%{version}
%{_bindir}/*
%{gemdir}/cache/less-%{version}.gem
%{gemdir}/specifications/less-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/spec
%exclude %{geminstdir}/.gitignore

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 1.2.21-1
- Initial package.

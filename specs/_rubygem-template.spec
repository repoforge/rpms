# $Id$
# Authority: shuff
# Upstream: UPSTREAMTAG

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/GEMNAME-%{version}

%global rubyabi 1.8

Summary: 
Name: rubygem-GEMNAME

Version: 
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/GEMNAME/

Source0: http://rubygems.org/downloads/GEMNAME-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(GEMNAME) = %{version}

%description


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
%doc %{geminstdir}/CHANGES %{geminstdir}/LICENSE %{geminstdir}/README
%doc %{geminstdir}/test
%doc %{gemdir}/doc/GEMNAME-%{version}
%doc %{geminstdir}/doc
%{_bindir}/*
%{gemdir}/cache/GEMNAME-%{version}.gem
%{gemdir}/specifications/GEMNAME-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/install.rb
%{geminstdir}/bin
%{geminstdir}/lib

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 
- Initial package.

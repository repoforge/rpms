# $Id$
# Authority: shuff
# Upstream: John W. Long <me$johnwlong,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/radius-%{version}

%global rubyabi 1.8

Summary: Tag-based template language for Ruby
Name: rubygem-radius

Version: 0.6.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/radius/

Source: http://rubygems.org/downloads/radius-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(radius) = %{version}

%description
Radius is a powerful tag-based template language for Ruby inspired by the
template languages used in MovableType and TextPattern. It uses tags similar to
XML, but can be used to generate any form of plain text (HTML, e-mail, etc…). 


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


find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/QUICKSTART.rdoc
%doc %{geminstdir}/README.rdoc
%doc %{gemdir}/doc/radius-%{version}
%{gemdir}/cache/radius-%{version}.gem
%{gemdir}/specifications/radius-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/tasks
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 0.6.1-1
- Initial package.

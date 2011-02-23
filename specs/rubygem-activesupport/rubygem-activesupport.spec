# $Id$
# Authority: shuff
# Upstream: Ruby On Rails list <rubyonrails-talk$googlegroups,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/activesupport-%{version}

%global rubyabi 1.8

Summary: Libraries and extensions from Ruby On Rails
Name: rubygem-activesupport

Version: 3.0.4
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org/

Source: http://rubygems.org/downloads/activesupport-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(activesupport) = %{version}
Provides: rubygem(active_support) = %{version}

%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization, time
zones, and testing.


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


find %{buildroot}%{geminstdir}/lib -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/lib -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/README.rdoc
%doc %{gemdir}/doc/activesupport-%{version}
%{gemdir}/cache/activesupport-%{version}.gem
%{gemdir}/specifications/activesupport-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/lib

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 3.0.4-1
- Initial package.

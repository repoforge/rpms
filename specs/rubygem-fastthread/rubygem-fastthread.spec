# $Id$
# Authority: shuff
# Upstream: MenTaLguY <mental$rydia,net>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/fastthread-%{version}

%global rubyabi 1.8

Summary: Optimized replacement for thread.rb primitives
Name: rubygem-fastthread

Version: 1.0.7
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/fastthread/

Source: http://rubygems.org/downloads/fastthread-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(fastthread) = %{version}

%description
Optimized replacement for thread.rb primitives.

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
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/Manifest
%doc %{geminstdir}/ext
%doc %{geminstdir}/fastthread.gemspec
%doc %{geminstdir}/test
%doc %{gemdir}/doc/fastthread-%{version}
%{gemdir}/cache/fastthread-%{version}.gem
%{gemdir}/specifications/fastthread-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/setup.rb
%{geminstdir}/lib
%exclude %{geminstdir}/.require_paths

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 1.0.7-1
- Initial package.

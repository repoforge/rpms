# $Id$
# Authority: shuff
# Upstream: Clifford Heath <clifford.heath$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/polyglot-%{version}

%global rubyabi 1.8

Summary: Allow custom language loaders to be hooked into Ruby's require
Name: rubygem-polyglot

Version: 0.3.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://polyglot.rubyforge.org/

Source: http://rubygems.org/downloads/polyglot-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}

Provides: rubygem(polyglot) = %{version}

%description
Polyglot provides a registry of file types that can be loaded by calling its
improved version of ‘require’. Each file extension that can be handled by a
custom loader is registered by calling Polyglot.register(“ext”, <class>), and
then you can simply require “somefile”, which will find and load “somefile.ext”
using your custom loader.

This supports the creation of DSLs having a syntax that is most appropriate to
their purpose, instead of abusing the Ruby syntax.

Required files are attempted first using the normal Ruby loader, and if that
fails, Polyglot conducts a search for a file having a supported extension.


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
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/License.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{gemdir}/doc/polyglot-%{version}
%{gemdir}/cache/polyglot-%{version}.gem
%{gemdir}/specifications/polyglot-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 0.3.1-1
- Initial package.

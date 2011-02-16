# $Id$
# Authority: shuff
# Upstream: Austin Ziegler <halostatue$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/mime-types-%{version}

%global rubyabi 1.8

Summary: Ruby port of Perl MIME::Types
Name: rubygem-mime-types

Version: 1.16
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/mime-types/

Source: http://rubygems.org/downloads/mime-types-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(archive-tar-minitar) >= 0.5
BuildRequires: rubygem(hoe) >= 1.8.3
BuildRequires: rubygem(nokogiri) >= 1.2
BuildRequires: rubygem(rcov) >= 0.8
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(archive-tar-minitar) >= 0.5
Requires: rubygem(hoe) >= 1.8.3
Requires: rubygem(nokogiri) >= 1.2
Requires: rubygem(rcov) >= 0.8
Provides: rubygem(mime-types) = %{version}

%description
MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copyright 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

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
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Install.txt
%doc %{geminstdir}/Licence.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{geminstdir}/mime-types.gemspec
%doc %{geminstdir}/test
%doc %{gemdir}/doc/mime-types-%{version}
%{gemdir}/cache/mime-types-%{version}.gem
%{gemdir}/specifications/mime-types-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/setup.rb
%{geminstdir}/lib

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 1.16-1
- Initial package.

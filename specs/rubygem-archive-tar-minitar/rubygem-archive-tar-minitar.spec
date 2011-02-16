# $Id$
# Authority: shuff
# Upstream: Austin Ziegler <halostatue$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/archive-tar-minitar-%{version}

%global rubyabi 1.8

Summary: Ruby library for dealing with POSIX tar files
Name: rubygem-archive-tar-minitar

Version: 0.5.2
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubygems.org/gems/archive-tar-minitar/

Source: http://rubygems.org/downloads/archive-tar-minitar-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(archive-tar-minitar) = %{version}

%description
Archive::Tar::Minitar is a pure-Ruby library and command-line utility that
provides the ability to deal with POSIX tar(1) archive files. The
implementation is based heavily on Mauricio Fernandez's implementation in
rpa-base, but has been reorganised to promote reuse in other projects.

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
%doc %{geminstdir}/ChangeLog
%doc %{geminstdir}/Install
%doc %{geminstdir}/README
%doc %{geminstdir}/tests
%doc %{gemdir}/doc/archive-tar-minitar-%{version}
%{_bindir}/*
%{gemdir}/cache/archive-tar-minitar-%{version}.gem
%{gemdir}/specifications/archive-tar-minitar-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib

%changelog
* Wed Feb 16 2011 Steve Huff <shuff@vecna.org> - 0.5.2-1
- Initial package.

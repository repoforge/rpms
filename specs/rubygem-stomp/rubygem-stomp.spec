# $Id$
# Authority: shuff
# Upstream: Johan Sorensen <johan$johansorensen,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/stomp-%{version}

%global rubyabi 1.8

Summary: Ruby implementation of the Stomp protocol
Name: rubygem-stomp

Version: 1.1.8
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/stomp/

Source: http://rubygems.org/downloads/stomp-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(stomp) = %{version}

%description
The Stomp project is the Streaming Text Orientated Messaging Protocol site (or
the Protocol Briefly Known as TTMP and Represented by the symbol :ttmp).

Stomp provides an interoperable wire format so that any of the available Stomp
Clients can communicate with any Stomp Message Broker to provide easy and
widespread messaging interop among languages, platforms and brokers.

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
find %{buildroot}%{geminstdir}/{examples,lib,spec,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{examples,lib,spec,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/stomp.gemspec
%doc %{gemdir}/doc/stomp-%{version}
%doc %{geminstdir}/examples
%doc %{geminstdir}/spec
%{_bindir}/*
%{gemdir}/cache/stomp-%{version}.gem
%{gemdir}/specifications/stomp-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Thu Mar 17 2011 Steve Huff <shuff@vecna.org> - 1.1.8-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: Francis Cianfrocca <blackhedd$gmail,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/eventmachine-%{version}

%global rubyabi 1.8

Summary: Event-processing library for Ruby
Name: rubygem-eventmachine

Version: 0.12.10
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://rubyeventmachine.com/

Source: http://rubygems.org/downloads/eventmachine-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel
BuildRequires: zlib-devel
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(eventmachine) = %{version}

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs to
specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal of
EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required. 

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


find %{buildroot}%{geminstdir}/{lib,tests} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,tests} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/README
%doc %{geminstdir}/eventmachine.gemspec
%doc %{gemdir}/doc/eventmachine-%{version}
%doc %{geminstdir}/docs
%doc %{geminstdir}/examples
%{gemdir}/cache/eventmachine-%{version}.gem
%{gemdir}/specifications/eventmachine-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/setup.rb
%{geminstdir}/ext
%{geminstdir}/java
%{geminstdir}/lib
%{geminstdir}/tasks
%{geminstdir}/tests
%{geminstdir}/web
%exclude %{geminstdir}/.gitignore

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 0.12.10-1
- Initial package.

# $Id$
# Authority: shuff
# Upstream: RightScale, Inc. <rubygems$rightscale,com>

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/right_http_connection-%{version}

%global rubyabi 1.8

Summary: RightScale's robust HTTP/S connection module
Name: rubygem-right_http_connection

Version: 1.2.4
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rightscale.rubyforge.org/

Source: http://rubygems.org/downloads/right_http_connection-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(right_http_connection) = %{version}

%description
Rightscale::HttpConnection is a robust HTTP/S library. It implements a retry
algorithm for low-level network errors.

Features:

* provides put/get streaming
* does configurable retries on connect and read timeouts, DNS failures, etc.
* HTTPS certificate checking


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
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%doc %{gemdir}/doc/right_http_connection-%{version}
%{gemdir}/cache/right_http_connection-%{version}.gem
%{gemdir}/specifications/right_http_connection-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/setup.rb
%{geminstdir}/lib

%changelog
* Wed Feb 23 2011 Steve Huff <shuff@vecna.org> - 1.2.4-1
- Initial package.

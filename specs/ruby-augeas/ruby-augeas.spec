# $Id$
# Authority: shuff

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")

%global rubyabi 1.8

Summary: Ruby bindings for Augeas.
Name: ruby-augeas

Version: 0.3.0
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://augeas.net/

Source: http://augeas.net/download/ruby/ruby-augeas-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: augeas-devel >= 0.5.1
BuildRequires: pkgconfig
BuildRequires: ruby-devel
BuildRequires: rubygem(rake)
Requires: ruby(abi) = %{rubyabi}
Provides: ruby(augeas) = %{version}

%description
Ruby bindings for Augeas.

%prep
%setup

%build
rake build

%install
%{__rm} -rf %{buildroot}

# gotta do it by hand
%{__install} -m0755 -d %{buildroot}%{ruby_sitearch}
%{__install} -m0755 -d %{buildroot}%{ruby_sitelib}
%{__install} -m0644 ext/augeas/_augeas.so %{buildroot}%{ruby_sitearch}
%{__install} -m0644 lib/augeas.rb %{buildroot}%{ruby_sitelib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc COPYING NEWS README.rdoc
%{ruby_sitearch}/*
%{ruby_sitelib}/*

%changelog
* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 0.3.0-1
- Initial package (ported from EPEL).

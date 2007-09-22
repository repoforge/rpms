# $Id$
# Authority: dag

%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")

%define real_name shadow

Summary: Ruby bindings for shadow password access
Name: ruby-shadow
Version: 1.4.1
Release: 1
License: Public Domain
Group: System Environment/Libraries
URL: http://ttsky.net/

Source: http://ttsky.net/src/ruby-shadow-%{version}.tar.gz
Patch0: ruby-shadow-1.4.1-cflags.patch
Patch1: ruby-shadow-1.4.1-struct.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby-devel
BuildRequires: ruby(abi) = 1.8
Requires: ruby(abi) = 1.8
Provides: ruby(shadow) = %{version}-%{release}

%description
Ruby bindings for shadow password access

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
ruby extconf.rb --with-cflags="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY README
%{ruby_sitearch}/shadow.so

%changelog
* Fri Sep 14 2007 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Initial package. (using DAR)

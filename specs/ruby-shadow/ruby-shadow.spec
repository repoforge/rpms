# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_ruby_api 1}
%{?el3:%define _without_ruby_api 1}
%{?rh9:%define _without_ruby_api 1}
%{?rh7:%define _without_ruby_api 1}
%{?el2:%define _without_ruby_api 1}

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
%{!?_without_ruby_api:BuildRequires: ruby(abi) = 1.8}
%{?_without_ruby_api:BuildRequires: ruby >= 1.8}
%{!?_without_ruby_api:Requires: ruby(abi) = 1.8}
%{?_without_ruby_api:Requires: ruby >= 1.8}
Provides: ruby(shadow) = %{version}-%{release}

%description
Ruby bindings for shadow password access

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p1

### Fix generated Makefile problem on EL4
%{__rm} -f depend

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
%doc HISTORY MANIFEST README*
%{ruby_sitearch}/shadow.so

%changelog
* Fri Sep 14 2007 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Added fix to generate Makefile on EL4. (Andreas Rogge)
- Added _without_ruby_api macro for EL4 and older. (Andreas Rogge)
- Initial package. (using DAR)

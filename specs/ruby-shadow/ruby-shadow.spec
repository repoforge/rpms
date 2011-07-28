# $Id$
# Authority: dag

### EL6 ships with ruby-shadow-1.4.1-13.el6 in rhn-tools-rhel-$arch-server-6
### Apparently nothing to worry about, they take it directly from EPEL

%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}
# This fails in mock since ruby doesn't exist in the default build env.
#%%{!?ruby_abi: %%define ruby_abi %%(ruby -rrbconfig -e "puts Config::CONFIG['ruby_version']")}

%{?el4:%define _without_ruby_api 1}
%{?el3:%define _without_ruby_api 1}

%define real_name shadow

Summary: Ruby bindings for shadow password access
Name: ruby-shadow
Version: 1.4.1
Release: 2%{?dist}
License: Public Domain
Group: System Environment/Libraries
URL: http://ttsky.net/

Source: http://ttsky.net/src/ruby-shadow-%{version}.tar.gz
Patch0: ruby-shadow-1.4.1-cflags.patch
Patch1: ruby-shadow-1.4.1-struct.patch
Patch2: ruby-shadow-1.4.1-depend.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby
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
%patch2 -p1

%{_bindir}/iconv -f EUCJP -t utf8 -o README.ja README.euc

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
* Tue Jun 28 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.1-2
- Added builddep on ruby, since it's not in the base by default.
- Synced with the latest version from EPEL.

* Fri Sep 14 2007 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Added fix to generate Makefile on EL4. (Andreas Rogge)
- Added _without_ruby_api macro for EL4 and older. (Andreas Rogge)
- Initial package. (using DAR)

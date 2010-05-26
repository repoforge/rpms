# $Id$
# Authority: shuff
# Upstream: Clifford Wolf <clifford$clifford,at>

%define make_opts prefix=%{_prefix} libdir=%{_lib}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")

Summary: stfl
Name: stfl
Version: 0.21
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.clifford.at/stfl

Source: http://www.clifford.at/stfl/stfl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel
BuildRequires: perl
BuildRequires: python-devel
BuildRequires: ruby-devel
# spl not yet packaged
# BuildRequires: spl-devel
BuildRequires: swig

%description
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and Ruby. The
public STFL API is only 14 simple function calls big and there are already
generic SWIG bindings. Thus is very easy to port STFL to additional scripting
languages.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package perl
Summary: Perl SWIG bindings for stfl
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl

%description perl
Install this package to use STFL in Perl programs.

%package python
Summary: Python SWIG bindings for stfl
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: python
Provides: python(stfl) = %{version}

%description python
Install this package to use STFL in Python programs.

%package ruby
Summary: Ruby SWIG bindings for stfl
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: ruby
Provides: ruby(stfl) = %{version}

%description ruby
Install this package to use STFL in Ruby programs.

# %package spl
# Summary: SPL SWIG bindings for stfl
# Group: Development/Libraries
# Requires: %{name} = %{version}-%{release}
# Requires: spl
# Provides: spl(stfl) = %{version}
# 
# %description spl
# Install this package to use STFL in SPL programs.

%prep
%setup

%build
%{__make} %{make_opts} %{?_smp_mflags} AM_CFLAGS=""

%install
%{__rm} -rf %{buildroot}
%{__make} install %{make_opts} DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc example.* perl5/example* python/example* ruby/example* spl/example*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/stfl.pc
%exclude %{_libdir}/*.a

%files perl
%defattr(-, root, root, 0755)
%{perl_vendorarch}/*.pm
%exclude %{perl_vendorarch}/example.pl
%{perl_vendorarch}/auto/stfl/stfl.*
%exclude %{perl_vendorarch}/auto/stfl/.packlist
%exclude %{perl_archlib}/*

%files python
%defattr(-, root, root, 0755)
%{python_sitearch}/*

%files ruby
%defattr(-, root, root, 0755)
%{ruby_sitearch}/*

# %files spl
# %defattr(-, root, root, 0755)
# 

%changelog
* Wed May 26 2010 Steve Huff <shuff@vecna.org> - 0.21-1
- Initial package (thanks to Philip Durbin).

# $Id$
# Authority: dag

Summary: Portable foreign function interface library
Name: libffi
Version: 3.0.9
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://sourceware.org/libffi/

Source: ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Compilers for high level languages generate code that follow certain
conventions. These conventions are necessary, in part, for separate
compilation to work. One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function. A
calling convention also specifies where the return value for a function
is found.

Some programs may not know at the time of compilation what arguments
are to be passed to a function. For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function. `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%post devel
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/libffi.info.gz

%preun devel
if [ $1 = 0 ] ;then
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/libffi.info.gz
fi

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog* LICENSE README
%{_libdir}/libffi.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/libffi.info*
%doc %{_mandir}/man3/ffi.3*
%doc %{_mandir}/man3/ffi_call.3*
%doc %{_mandir}/man3/ffi_prep_cif.3*
%{_libdir}/libffi.so
%{_libdir}/libffi-%{version}/
%{_libdir}/pkgconfig/libffi.pc
%exclude %{_libdir}/libffi.la

%changelog
* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 3.0.9-1
- Initial package. (using DAR)

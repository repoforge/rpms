# $Id$
# Authority: shuff
# Upstream: Andy Lester <andy$petdance,com>

Summary: Fork of tidy/libtidy
Name: tidyp
Version: 1.02
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://tidyp.com/

Source: http://github.com/downloads/petdance/tidyp/tidyp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, gcc-c++, make, autoconf, automake
BuildRequires: libtool

%description
tidyp is a fork of tidy on SourceForge at http://tidy.sf.net.  The
library name is "tidyp", and the command-line tool is also "tidyp"
but all internal API stays the same.

tidyp will validate your HTML, and output cleaned-up HTML.


%package devel
Summary: Headers and development files for tidyp.
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}

%description devel
Install this package if you want to develop software that uses libtidyp.
%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-access \
    --enable-utf16 \
    --enable-asian
%{__make} %{?_smp_mflags} 

%install
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL README
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Wed Jun 30 2010 Steve Huff <shuff@vecna.org> - 1.02-1
- Initial package.

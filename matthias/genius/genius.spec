# Authority: dag

Summary: An advanced calculator.
Name: genius
Version: 0.5.6
Release: 0
License: GPL
Group: Applications/Engineering
URL: http://www.5z.com/jirka/genius.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel, vte-devel, libgnomeui-devel >= 2.0
BuildRequires: gtksourceview-devel >= 0.3, libglade2-devel >= 1.99

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/genius/
%{_libdir}/genius/
%{_libexecdir}/*
%{_includedir}/genius/
%{_datadir}/applications/*.desktop

%changelog
* Mon Nov 24 2003 Dag Wieers <dag@wieers.com> - 0.5.6-0
- Initial package. (using DAR)

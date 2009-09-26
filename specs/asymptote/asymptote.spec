# $Id$
# Authority: dries
# Upstream: John Bowman <imaging$math,ualberta,ca>

Summary: Descriptive vector graphics language
Name: asymptote
Version: 1.26
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://asymptote.sourceforge.net/

Source: http://dl.sf.net/asymptote/asymptote-%{version}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgc-devel >= 6.7, libgc >= 6.7, fftw-devel
BuildRequires: ncurses-devel, readline-devel, gcc-c++
BuildRequires: libsigsegv-devel, tetex-latex, ghostscript

%description
Asymptote is a powerful descriptive vector graphics language for
technical drawing, inspired by MetaPost but with an improved C++-like
syntax. It provides for figures the same high-quality level of
typesetting that LaTeX does for scientific text. Asymptote is a
programming language as opposed to just a graphics program. It can
exploit the best features of script (command-driven) and graphical
user interface (GUI) methods. High-level graphics commands are
implemented in the language itself, allowing them to be easily
tailored to specific applications.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Asymptote
Comment=Vector graphics language
Exec=xasy
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Office;
EOF

%{__perl} -pi.orig -e 's|<gc.h>|<gc/gc.h>|' configure memory.h

%build
%configure \
    --enable-gc="system"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop
%{__mv} %{buildroot}%{_docdir}/asymptote rpmdocs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL LICENSE README TODO rpmdocs/*
%doc %{_mandir}/man1/asy*
%doc %{_mandir}/man1/xasy*
%{_datadir}/texmf/tex/latex/asymptote/
%{_bindir}/asy
%{_bindir}/xasy
%{_datadir}/asymptote/
%{_datadir}/applications/*-asymptote.desktop

%changelog
* Sun Jul 29 2007 Dag Wieers <dag@wieers.com> - 1.26-2
- Build against libgc-7.0.

* Fri Apr 20 2007 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Fri Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Fri Apr 28 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Updated to release 1.00.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 0.97-1
- Initial package.

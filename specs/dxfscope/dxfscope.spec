# $Id$
# Authority: dries

# Screenshot: http://wildspark.com/dxfscope/screenshot-city-thumb.png
# ScreenshotURL: http://wildspark.com/dxfscope/

Summary: Viewer for DXF drawings
Name: dxfscope
Version: 0.2
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://wildspark.com/dxfscope/

Source: http://wildspark.com/dxfscope/dxfscope-current.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel

%description
DXFscope is a viewer for DXF drawings. It supports the most commonly used
entities of the DXF specification.

%prep
%setup

%build
%{__perl} -pi.orig -e '
		s|^(BINDIR)=.+$|$1=\$(bindir)|;
		s|^(SHAREDIR)=.+$|$1=\$(datadir)/dxfscope|;
		s|-L/usr/X11R6/lib|-L%{_prefix}/X11R6/%{_lib}|;
		s| -oroot | |;
	' Makefile
%{__make} %{?_smp_mflags} \
	datadir="%{_datadir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README COPYING HACKING TODO
%{_bindir}/dxfscope
%{_datadir}/dxfscope/

%changelog
* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.2-3
- Cosmetic cleanup.
- Fixes for x86_64.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.2-3
- install require fix for fedora core 2
  Thanks to Jochen Schlick for reporting the bug!

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.2-2
- cleanup of spec file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.2-1
- first packaging for Fedora Core 1
 

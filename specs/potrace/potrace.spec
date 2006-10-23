# $Id$
# Authority: dag
# Upstream: Peter Selinger <selinger$users,sourceforge,net>

Summary: Transforms bitmaps into vector graphics
Name: potrace
Version: 1.7
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://potrace.sourceforge.net/

Source: http://potrace.sourceforge.net/download/potrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.  The input is a portable bitmap
(PBM), and the default output is an encapsulated PostScript file
(EPS). A typical use is to create EPS files from scanned data, such as
company or university logos, handwritten notes, etc.  The resulting
image is not "jaggy" like a bitmap, but smooth, and it can be scaled
to any resolution. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%doc %{_mandir}/man1/mkbitmap.1*
%doc %{_mandir}/man1/potrace.1*
%{_bindir}/mkbitmap
%{_bindir}/potrace

%changelog
* Mon Oct 23 2006 Dag Wieers <dag@wieers.com> - 1.7-1
- Initial package. (using DAR)

# $Id$
# Authority: dag

Summary: Tools for SWF (Flash) animations under linux
Name: swftools
Version: 0.9.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.swftools.org/

Source: http://www.swftools.org/swftools-%{version}.tar.gz
Patch0: swftools-0.9.1-destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, flex, gcc >= 3.0, zlib-devel, libjpeg-devel, t1lib-devel, giflib-devel
#BuildRequires: libavifile-devel
Conflicts: ming

%description
SWF Tools is a collection of SWF manipulation and generation utilities.

%prep
%setup
%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
#%doc %{_mandir}/man1/avi2swf.1*
%doc %{_mandir}/man1/font2swf.1*
%doc %{_mandir}/man1/gif2swf.1*
%doc %{_mandir}/man1/jpeg2swf.1*
%doc %{_mandir}/man1/pdf2swf.1*
%doc %{_mandir}/man1/png2swf.1*
%doc %{_mandir}/man1/swfbbox.1*
%doc %{_mandir}/man1/swfc.1*
%doc %{_mandir}/man1/swfcombine.1*
%doc %{_mandir}/man1/swfdump.1*
%doc %{_mandir}/man1/swfextract.1*
%doc %{_mandir}/man1/swfstrings.1*
%doc %{_mandir}/man1/wav2swf.1*
%doc %{_mandir}/man1/as3compile.1*
%doc %{_mandir}/man1/swfrender.1*
#%{_bindir}/avi2swf
%{_bindir}/font2swf
%{_bindir}/gif2swf
%{_bindir}/jpeg2swf
%{_bindir}/pdf2swf
%{_bindir}/png2swf
%{_bindir}/swfbbox
%{_bindir}/swfc
%{_bindir}/swfcombine
%{_bindir}/swfdump
%{_bindir}/swfextract
%{_bindir}/swfstrings
%{_bindir}/swfrender
%{_bindir}/wav2swf
%{_bindir}/as3compile
%{_datadir}/swftools/

%changelog
* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Initial package. (using DAR)

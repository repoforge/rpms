# $Id$
# Authority: matthias

%define real_version 0.3-4

Summary: DVD subtitle ripper
Name: subtitleripper
Version: 0.3.4
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://subtitleripper.sourceforge.net/
Source: http://dl.sf.net/subtitleripper/subtitleripper-%{real_version}.tgz
Patch0: subtitleripper-0.3.4-20041108cvs.patch
Patch1: subtitleripper-0.3.4-libnetpbm.patch
Patch2: subtitleripper-0.3.4-nopng.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: netpbm, transcode
BuildRequires: netpbm, netpbm-devel, libpng-devel, zlib-devel

%description
Converts DVD subtitles into text format (e.g. subrip) or VobSub.


%prep
%setup -n %{name}
%patch0 -p1 -b .20041108cvs
%patch1 -p1 -b .libnetpbm
%patch2 -p1 -b .nopng


%build
%{__make} %{?_smp_mflags} COPT="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 pgm2txt srttool subtitle2pgm subtitle2vobsub \
    %{buildroot}%{_bindir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README*
%{_bindir}/*


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.3.4-3
- Release bump to drop the disttag number in FC5 build.

* Fri Apr 22 2005 Matthias Saou <http://freshrpms.net/> 0.3.4-2
- Update to 20041108 CVS (with a patch).
- Set COPT to use optflags.
- Disable png support for now as it errors out on FC4. Fix required!

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.3.4-1
- Update to 0.3-4.
- Added patch to fix libppm vs. libnetpbm issue.
- Rebuild for Fedora Core 2.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3-2 (numbered as 0.3.2).
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.
- Rebuilt for Red Hat Linux 9.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Thu Oct 17 2002 Michel Alexandre Salim <salimma@freeshell.org>
- Initial RPM release.


# $Id$

%define xmms_inputdir %(xmms-config --input-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Input)

Summary: X MultiMedia System input plugin to play Windows Media Audio files
Name: xmms-wma
Version: 1.0.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://mcmcc.bat.ru/xmms-wma/
Source: http://mcmcc.bat.ru/xmms-wma/xmms-wma-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.1, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel

%description
X MultiMedia System input plugin to play Windows Media Audio, aka WMA files.
This plug-in is written using the ffmpeg library (http://ffmpeg.sf.net)
written by Fabrice Bellard (to be exact, strongly advanced library).
Everything besides wma format support was removed from it to make it lighter.
Tag informations are converted from unicode to your system locale.


%prep
%setup


%build
%ifnarch %{ix86}
%{__perl} -pi.orig -e 's|#define ARCH_X86.*|#undef ARCH_X86|g;
                  s|#define __CPU__.*|#undef __CPU__|g' \
    ffmpeg-strip-wma/config.h
%endif
%{__perl} -pi.orig -e 's| (-shared)| $1 -fPIC|; s| (-DX86)| $1 -fPIC|;' Makefile.inc
%{__make} %{?_smp_mflags} \
	OPTFLAGS="%{optflags} -fPIC"


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 libwma.so %{buildroot}%{xmms_inputdir}/libwma.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%lang(ru) %doc readme.rus
%doc readme.eng COPYING
%{xmms_inputdir}/libwma.so


%changelog
* Mon Jun  7 2004 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Initial rpm package.


# $Id$
# Authority: dries
# Upstream: Thomas Eschenbacher <thomas,eschenbacher$gmx,de>

Summary: Sound editor
Name: kwave
Version: 0.7.10
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kwave.sourceforge.net/

Source: http://dl.sf.net/kwave/kwave-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libtool, gettext, recode, gsl-devel, kdelibs-devel, ImageMagick, kdesdk
BuildRequires: libmad-devel, id3lib-devel, flac-devel, kdemultimedia-devel, cmake
Requires: ImageMagick

%description
Kwave is a 24-bit sound editor that allows simple operations, such as cut,
copy, and paste. Some more effect functions with little complexity (Simple
Filtering, Delay) are also implemented. More sophisticated analysis
functions (spectrograms, sonagrams, pitch determination) are underway or
partially done.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%{__perl} -pi -e "s|logowidget.h|LogoWidget.h|g;" ./plugins/about/KwaveAboutDialogBase.ui
%{__perl} -pi -e "s|bitratewidget.h|BitrateWidget.h|g;" ./plugins/fileinfo/CompressionWidgetBase.ui
%{__perl} -pi -e "s|compressionwidget.h|CompressionWidget.h|g;" ./plugins/fileinfo/FileInfoDlg.ui
%{__perl} -pi -e "s|keywordwidget.h|KeywordWidget.h|g;" ./plugins/fileinfo/FileInfoDlg.ui
%{__perl} -pi -e "s|scalewidget.h|libgui/ScaleWidget.h|g;" ./plugins/lowpass/LowPassDlg.ui ./plugins/notch_filter/NotchFilterDlg.ui
%{__perl} -pi -e "s|frequencyresponsewidget.h|libgui/FrequencyResponseWidget.h|g;" ./plugins/lowpass/LowPassDlg.ui ./plugins/notch_filter/NotchFilterDlg.ui
%{__perl} -pi -e "s|invertablespinbox.h|libgui/InvertableSpinBox.h|g;" ./plugins/pitch_shift/PitchShiftDlg.ui
%{__perl} -pi -e "s|hmstimewidget.h|libgui/HMSTimeWidget.h|g;" ./plugins/record/RecordDlg.ui
%{__perl} -pi -e "s|levelmeter.h|LevelMeter.h|g;" ./plugins/record/RecordDlg.ui
%{__perl} -pi -e "s|selecttimewidget.h|libgui/SelectTimeWidget.h|g;" ./plugins/selectrange/SelectRangeDlg.ui

%build
cmake .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS README TODO
%doc %{_docdir}/HTML/*/kwave/
%{_bindir}/kwave
%{_libdir}/libkwave.so.*
%{_libdir}/libkwavegui.so.*
%{_datadir}/applnk/Multimedia/kwave.desktop
%{_datadir}/apps/kwave/
%{_datadir}/icons/*/*/apps/kwave.png
%{_datadir}/mimelnk/audio/*.desktop

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libkwave.so
%{_libdir}/libkwavegui.so

%changelog
* Sat Aug 25 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.10-1
- Updated to release 0.7.10.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.7-1
- Updated to release 0.7.7.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.5-1
- Initial package.
